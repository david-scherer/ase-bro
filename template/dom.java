package com.example.demo.hyperloop;

import com.example.demo.hyperloop.model.Obstacle;
import com.example.demo.hyperloop.model.Target;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/hyperloop")
public class HyperloopController {

    @Autowired
    private ObstacleRepository obstacleRepository;

    @Autowired
    private TargetRepository targetRepository;


    @GetMapping("/obstacle/{id}/targets")
    public ResponseEntity<List<Target>> getAccessiblePoints(@PathVariable Long id, @RequestParam List<Long> targetIds) {

        Optional<Obstacle> obstacleOptional = obstacleRepository.findById(id);
        if (obstacleOptional.isEmpty()) {
            return ResponseEntity.status(HttpStatus.NOT_FOUND).build();
        } else {
            List<Target> accessiblePoints = new ArrayList<>();
            Obstacle obstacle = obstacleOptional.get();

            for (Long targetID : targetIds) {
                Target target = targetRepository.findById(targetID).orElse(null);
                if (target == null) {
                    return ResponseEntity.status(HttpStatus.NOT_FOUND).build();
                }
                if (!(isBlockedByLineObstacle(target, obstacle) && isBlockedByTwoPointsObstacle(target, obstacle))) {
                    accessiblePoints.add(target);
                }
            }
            return ResponseEntity.status(HttpStatus.OK).body(accessiblePoints);
        }
    }

    private boolean isBlockedByLineObstacle(Target target, Obstacle obstacle) {
        if (obstacle.getLine() > 0) {
            return target.getY() > obstacle.getLine();
        } else {
            return target.getY() < obstacle.getLine();
        }
    }

    private boolean isBlockedByTwoPointsObstacle(Target target, Obstacle obstacle) {
        Integer oax = obstacle.getPointA().getX();
        Integer oay = obstacle.getPointA().getY();
        Integer obx = obstacle.getPointB().getX();
        Integer oby = obstacle.getPointB().getY();

        Integer tx = target.getX();
        Integer ty = target.getY();

        double anglePointA = Math.toDegrees(Math.atan2(oay, oax));
        double anglePointB = Math.toDegrees(Math.atan2(oby, obx));

        double angleTarget = Math.toDegrees(Math.atan2(ty, tx));


        if (obstacle.getPointA().getY() > 0) {
            return
                    (angleTarget > anglePointA && angleTarget < anglePointB) ||
                    (angleTarget > anglePointB && angleTarget < anglePointA)
                    ;
        } else {
            return
                    (angleTarget < anglePointA && angleTarget > anglePointB) ||
                    (angleTarget < anglePointB && angleTarget > anglePointA)
                    ;
        }
    }
}